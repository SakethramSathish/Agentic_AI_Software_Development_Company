import { motion, AnimatePresence } from 'framer-motion'
import { X } from 'lucide-react'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import CodeBlock from '../ui/CodeBlock'
import { AGENTS } from '../../hooks/useAgentPipeline'

/**
 * Slide-out panel showing the selected agent's output.
 */
export default function AgentOutputPanel({ agentKey, output, onClose }) {
  const agent = AGENTS.find(a => a.key === agentKey)
  if (!agent) return null

  // Detect if content looks like code
  const isCodeOutput = agentKey === 'backend_dev' || agentKey === 'frontend_dev'

  return (
    <AnimatePresence>
      <motion.div
        key={agentKey}
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        exit={{ opacity: 0, y: 20 }}
        transition={{ duration: 0.3 }}
        className="brutal-card overflow-hidden"
      >
        {/* Header */}
        <div className={`${agent.color} ${agent.textColor} px-5 py-4 flex items-center justify-between border-b-[3px] border-[var(--border-color)]`}>
          <div className="flex items-center gap-3">
            <span className="text-2xl">{agent.emoji}</span>
            <div>
              <h3 className="font-heading text-lg font-extrabold uppercase tracking-wide">
                {agent.label}
              </h3>
              <p className="text-xs font-body opacity-80">Agent Output</p>
            </div>
          </div>
          <motion.button
            whileHover={{ scale: 1.1 }}
            whileTap={{ scale: 0.9 }}
            onClick={onClose}
            className="border-2 border-current p-1 hover:opacity-70"
          >
            <X size={18} />
          </motion.button>
        </div>

        {/* Content */}
        <div className="p-5 max-h-[500px] overflow-y-auto" style={{ background: 'var(--bg-card)' }}>
          {output ? (
            isCodeOutput ? (
              <CodeBlock code={output} language="python" />
            ) : (
              <div className="markdown-content">
                <ReactMarkdown remarkPlugins={[remarkGfm]}>
                  {output}
                </ReactMarkdown>
              </div>
            )
          ) : (
            <p className="text-sm italic" style={{ color: 'var(--text-secondary)' }}>
              No output available
            </p>
          )}
        </div>
      </motion.div>
    </AnimatePresence>
  )
}
