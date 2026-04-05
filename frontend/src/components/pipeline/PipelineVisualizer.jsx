import { motion, AnimatePresence } from 'framer-motion'
import AgentNode from './AgentNode'
import { ArrowRight } from 'lucide-react'

/**
 * Pipeline Visualizer — horizontal flow of agent nodes connected by arrows.
 * The star feature: animated agent pipeline with real-time status.
 */
export default function PipelineVisualizer({ agents, getAgentStatus, selectedAgent, onSelectAgent }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4 }}
      className="brutal-card p-6 overflow-x-auto"
    >
      {/* Title */}
      <h2 className="font-heading text-xl font-extrabold uppercase tracking-wide mb-6"
          style={{ color: 'var(--text-primary)' }}>
        🔄 Agent Pipeline
      </h2>

      {/* Pipeline Flow */}
      <div className="flex items-center gap-2 min-w-max pb-2">
        {agents.map((agent, index) => (
          <div key={agent.key} className="flex items-center gap-2">
            <AgentNode
              agent={agent}
              status={getAgentStatus(agent.key)}
              isSelected={selectedAgent === agent.key}
              onClick={() => getAgentStatus(agent.key) === 'done' && onSelectAgent(agent.key)}
            />

            {/* Connector arrow */}
            {index < agents.length - 1 && (
              <motion.div
                initial={{ opacity: 0 }}
                animate={{
                  opacity: getAgentStatus(agent.key) === 'done' ? 1 : 0.3,
                }}
                transition={{ duration: 0.3 }}
              >
                <ArrowRight
                  size={20}
                  className="flex-shrink-0"
                  style={{ color: 'var(--border-color)' }}
                />
              </motion.div>
            )}
          </div>
        ))}
      </div>

      {/* Status bar */}
      <div className="mt-4 pt-4 border-t-[3px] border-[var(--border-color)] flex items-center justify-between">
        <p className="text-sm font-body" style={{ color: 'var(--text-secondary)' }}>
          {agents.filter(a => getAgentStatus(a.key) === 'done').length} / {agents.length} agents completed
        </p>
        <p className="text-xs font-heading font-bold uppercase" style={{ color: 'var(--text-secondary)' }}>
          Click a completed agent to view output
        </p>
      </div>
    </motion.div>
  )
}
