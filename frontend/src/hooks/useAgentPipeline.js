import { useState, useCallback, useRef } from 'react'
import { streamPipeline } from '../api/client'

/**
 * Agent metadata — order, colors, icons for the pipeline.
 */
export const AGENTS = [
  { key: 'ceo',              label: 'CEO',               emoji: '🧠', color: 'bg-brutal-yellow',  textColor: 'text-black' },
  { key: 'product_manager',  label: 'Product Manager',   emoji: '📦', color: 'bg-brutal-orange',  textColor: 'text-black' },
  { key: 'system_architect', label: 'System Architect',  emoji: '🏗️', color: 'bg-brutal-blue',    textColor: 'text-black' },
  { key: 'cto',              label: 'CTO',               emoji: '👔', color: 'bg-brutal-purple',  textColor: 'text-white' },
  { key: 'backend_dev',      label: 'Backend Dev',       emoji: '💻', color: 'bg-brutal-green',   textColor: 'text-black' },
  { key: 'frontend_dev',     label: 'Frontend Dev',      emoji: '🎨', color: 'bg-brutal-pink',    textColor: 'text-white' },
  { key: 'ai_engineer',      label: 'AI Engineer',       emoji: '🤖', color: 'bg-brutal-red',     textColor: 'text-white' },
  { key: 'qa',               label: 'QA Engineer',       emoji: '🧪', color: 'bg-brutal-amber',   textColor: 'text-black' },
  { key: 'code_reviewer',    label: 'Code Reviewer',     emoji: '🧾', color: 'bg-brutal-indigo',  textColor: 'text-white' },
  { key: 'documentation',    label: 'Documentation',     emoji: '📚', color: 'bg-brutal-teal',    textColor: 'text-black' },
]

export function useAgentPipeline() {
  const [agentStates, setAgentStates] = useState({})   // { [agentKey]: { status, output } }
  const [isRunning, setIsRunning] = useState(false)
  const [isComplete, setIsComplete] = useState(false)
  const [error, setError] = useState(null)
  const [currentAgent, setCurrentAgent] = useState(null)
  const [selectedAgent, setSelectedAgent] = useState(null)
  const completedRef = useRef(new Set())

  const runPipeline = useCallback(async (idea) => {
    // Reset state
    setAgentStates({})
    setIsRunning(true)
    setIsComplete(false)
    setError(null)
    setSelectedAgent(null)
    completedRef.current = new Set()

    // Mark first agent as running
    setCurrentAgent('ceo')

    await streamPipeline(idea, {
      onAgentUpdate: (event) => {
        const { agent, output } = event

        // Mark this agent as done
        completedRef.current.add(agent)
        setAgentStates(prev => ({
          ...prev,
          [agent]: { status: 'done', output: output || '' },
        }))

        // Determine next agent in pipeline
        const currentIndex = AGENTS.findIndex(a => a.key === agent)
        const nextAgent = AGENTS[currentIndex + 1]
        setCurrentAgent(nextAgent ? nextAgent.key : null)
      },

      onComplete: () => {
        setIsRunning(false)
        setIsComplete(true)
        setCurrentAgent(null)
      },

      onError: (errMsg) => {
        setIsRunning(false)
        setError(errMsg)
        setCurrentAgent(null)
      },
    })
  }, [])

  // Compute status for each agent
  const getAgentStatus = useCallback((agentKey) => {
    if (agentStates[agentKey]?.status === 'done') return 'done'
    if (currentAgent === agentKey) return 'running'
    return 'idle'
  }, [agentStates, currentAgent])

  return {
    agents: AGENTS,
    agentStates,
    isRunning,
    isComplete,
    error,
    currentAgent,
    selectedAgent,
    setSelectedAgent,
    runPipeline,
    getAgentStatus,
  }
}
