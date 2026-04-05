import { motion } from 'framer-motion'

/**
 * Neo-Brutalist Card — thick black border, hard offset shadow, hover lift.
 */
export default function BrutalCard({
  children,
  className = '',
  color = '',
  hoverable = true,
  onClick,
  ...props
}) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 15 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3 }}
      whileHover={hoverable ? { x: -2, y: -2 } : {}}
      onClick={onClick}
      className={`brutal-card p-5 ${color} ${onClick ? 'cursor-pointer' : ''} ${className}`}
      {...props}
    >
      {children}
    </motion.div>
  )
}
