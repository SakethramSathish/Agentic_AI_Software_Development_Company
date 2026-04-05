import { useState } from 'react'
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter'
import { oneDark } from 'react-syntax-highlighter/dist/esm/styles/prism'
import { Copy, Check } from 'lucide-react'

/**
 * Neo-Brutalist code block with syntax highlighting and copy button.
 */
export default function CodeBlock({ code, language = 'python' }) {
  const [copied, setCopied] = useState(false)

  const handleCopy = async () => {
    await navigator.clipboard.writeText(code)
    setCopied(true)
    setTimeout(() => setCopied(false), 2000)
  }

  return (
    <div className="relative brutal-card p-0 overflow-hidden" style={{ boxShadow: '4px 4px 0px 0px var(--shadow-color)' }}>
      {/* Header bar */}
      <div className="flex items-center justify-between px-4 py-2 border-b-[3px] border-[var(--border-color)]"
           style={{ background: 'var(--bg-secondary)' }}>
        <span className="font-heading text-xs font-bold uppercase tracking-wider" style={{ color: 'var(--text-secondary)' }}>
          {language}
        </span>
        <button
          onClick={handleCopy}
          className="flex items-center gap-1 text-xs font-bold uppercase hover:opacity-70 transition-opacity"
          style={{ color: 'var(--text-secondary)' }}
        >
          {copied ? <Check size={14} /> : <Copy size={14} />}
          {copied ? 'Copied!' : 'Copy'}
        </button>
      </div>

      {/* Code content */}
      <SyntaxHighlighter
        language={language}
        style={oneDark}
        customStyle={{
          margin: 0,
          padding: '1rem',
          fontSize: '0.85rem',
          borderRadius: 0,
          background: '#1e1e2e',
        }}
        wrapLongLines
      >
        {code || '// No code generated'}
      </SyntaxHighlighter>
    </div>
  )
}
