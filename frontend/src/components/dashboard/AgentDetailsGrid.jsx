import { motion } from 'framer-motion'
import BrutalCard from '../ui/BrutalCard'
import Badge from '../ui/Badge'
import { AGENTS } from '../../hooks/useAgentPipeline'
import { ChevronRight } from 'lucide-react'

/**
 * Grid of all completed agent outputs — click to expand.
 */
export default function AgentDetailsGrid({ agentStates, onSelectAgent }) {
  const completedAgents = AGENTS.filter(a => agentStates[a.key]?.status === 'done')

  if (completedAgents.length === 0) return null

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.4, delay: 0.2 }}
    >
      <h2 className="font-heading text-xl font-extrabold uppercase tracking-wide mb-4"
          style={{ color: 'var(--text-primary)' }}>
        📋 Agent Outputs
      </h2>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {completedAgents.map((agent, index) => (
          <motion.div
            key={agent.key}
            initial={{ opacity: 0, y: 15 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.05 }}
          >
            <BrutalCard
              onClick={() => onSelectAgent(agent.key)}
              className="h-full"
            >
              {/* Agent header */}
              <div className="flex items-center justify-between mb-3">
                <div className="flex items-center gap-2">
                  <span className="text-xl">{agent.emoji}</span>
                  <h3 className="font-heading text-sm font-bold uppercase tracking-wide"
                      style={{ color: 'var(--text-primary)' }}>
                    {agent.label}
                  </h3>
                </div>
                <Badge color={agent.color} textColor={agent.textColor}>
                  Done
                </Badge>
              </div>

              {/* Preview */}
              <p className="text-xs font-body leading-relaxed line-clamp-3 mb-3"
                 style={{ color: 'var(--text-secondary)' }}>
                {agentStates[agent.key]?.output?.slice(0, 150) || 'No output'}...
              </p>

              {/* View more */}
              <div className="flex items-center gap-1 text-xs font-heading font-bold uppercase"
                   style={{ color: 'var(--text-primary)' }}>
                View Full Output
                <ChevronRight size={14} />
              </div>
            </BrutalCard>
          </motion.div>
        ))}
      </div>
    </motion.div>
  )
}
