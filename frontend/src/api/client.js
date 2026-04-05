/**
 * SSE streaming client for the agentic pipeline.
 * Parses Server-Sent Events from the FastAPI backend.
 */

const API_BASE = '/api'

export async function streamPipeline(idea, { onAgentUpdate, onComplete, onError }) {
  try {
    const response = await fetch(`${API_BASE}/run`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ idea }),
    })

    if (!response.ok) {
      const err = await response.json().catch(() => ({ detail: 'Server error' }))
      throw new Error(err.detail || `HTTP ${response.status}`)
    }

    const reader = response.body.getReader()
    const decoder = new TextDecoder()
    let buffer = ''

    while (true) {
      const { done, value } = await reader.read()
      if (done) break

      buffer += decoder.decode(value, { stream: true })

      // Split on double newlines (SSE event boundary)
      const parts = buffer.split('\n\n')
      buffer = parts.pop() // keep incomplete event in buffer

      for (const part of parts) {
        if (!part.trim()) continue

        const lines = part.split('\n')
        let eventType = 'message'
        let data = ''

        for (const line of lines) {
          if (line.startsWith('event:')) {
            eventType = line.slice(6).trim()
          } else if (line.startsWith('data:')) {
            data = line.slice(5).trim()
          }
        }

        if (!data) continue

        try {
          const parsed = JSON.parse(data)

          if (eventType === 'agent_update') {
            onAgentUpdate?.(parsed)
          } else if (eventType === 'complete') {
            onComplete?.()
          } else if (eventType === 'error') {
            onError?.(parsed.error || 'Unknown error')
          }
        } catch {
          console.warn('Failed to parse SSE data:', data)
        }
      }
    }

    // Handle remaining buffer
    if (buffer.trim()) {
      onComplete?.()
    }
  } catch (err) {
    onError?.(err.message)
  }
}

export async function checkHealth() {
  try {
    const res = await fetch(`${API_BASE}/health`)
    return res.ok
  } catch {
    return false
  }
}
