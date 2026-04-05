import { motion } from 'framer-motion'
import { Check, Loader2 } from 'lucide-react'

/**
 * Individual agent node in the pipeline visualizer.
 * States: idle → running (pulsing) → done (checkmark).
 */
export default function AgentNode({ agent, status, isSelected, onClick }) {
  const isIdle = status === 'idle'
  const isRunning = status === 'running'
  const isDone = status === 'done'

  return (
    <motion.button
      onClick={onClick}
      disabled={isIdle}
      initial={{ scale: 0.8, opacity: 0 }}
      animate={{ scale: 1, opacity: 1 }}
      whileHover={isDone ? { x: -2, y: -2 } : {}}
      whileTap={isDone ? { x: 1, y: 1 } : {}}
      className={`
        relative flex flex-col items-center gap-2 p-3 min-w-[90px]
        border-[3px] border-[var(--border-color)] font-heading
        transition-all duration-200
        ${isDone
          ? `${agent.color} cursor-pointer`
          : isRunning
            ? `${agent.color} animate-pulse-brutal`
            : 'bg-[var(--bg-secondary)] opacity-50 cursor-not-allowed'
        }
        ${isSelected ? 'ring-4 ring-black ring-offset-2' : ''}
      `}
      style={{
        boxShadow: isDone || isRunning
          ? '4px 4px 0px 0px var(--shadow-color)'
          : '2px 2px 0px 0px var(--shadow-color)',
      }}
    >
      {/* Status indicator */}
      <div className="absolute -top-2 -right-2">
        {isDone && (
          <motion.div
            initial={{ scale: 0 }}
            animate={{ scale: 1 }}
            className="bg-brutal-green border-2 border-[var(--border-color)] rounded-full p-0.5"
          >
            <Check size={12} className="text-black" />
          </motion.div>
        )}
        {isRunning && (
          <motion.div
            animate={{ rotate: 360 }}
            transition={{ duration: 1, repeat: Infinity, ease: 'linear' }}
            className="bg-white border-2 border-[var(--border-color)] rounded-full p-0.5"
          >
            <Loader2 size={12} className="text-black" />
          </motion.div>
        )}
      </div>

      {/* Emoji */}
      <span className="text-xl">{agent.emoji}</span>

      {/* Label */}
      <span className={`text-[0.6rem] font-bold uppercase tracking-wider text-center leading-tight ${isDone || isRunning ? agent.textColor : ''}`}>
        {agent.label}
      </span>
    </motion.button>
  )
}
