import { motion } from 'framer-motion'

/**
 * Neo-Brutalist Button component.
 * Thick borders, hard shadows, press-down animation.
 */
export default function Button({
  children,
  onClick,
  disabled = false,
  variant = 'primary',
  size = 'md',
  className = '',
  ...props
}) {
  const variants = {
    primary: 'bg-brutal-yellow text-black',
    secondary: 'bg-brutal-purple text-white',
    danger: 'bg-brutal-red text-white',
    ghost: 'bg-transparent text-[var(--text-primary)]',
  }

  const sizes = {
    sm: 'px-3 py-1.5 text-xs',
    md: 'px-5 py-2.5 text-sm',
    lg: 'px-8 py-4 text-base',
  }

  return (
    <motion.button
      whileHover={!disabled ? { x: -2, y: -2 } : {}}
      whileTap={!disabled ? { x: 2, y: 2 } : {}}
      onClick={onClick}
      disabled={disabled}
      className={`brutal-btn ${variants[variant]} ${sizes[size]} ${className}`}
      {...props}
    >
      {children}
    </motion.button>
  )
}
