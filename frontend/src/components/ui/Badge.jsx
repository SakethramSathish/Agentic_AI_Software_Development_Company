/**
 * Neo-Brutalist Badge for labels and status indicators.
 */
export default function Badge({ children, color = 'bg-brutal-yellow', textColor = 'text-black', className = '' }) {
  return (
    <span className={`brutal-badge ${color} ${textColor} ${className}`}>
      {children}
    </span>
  )
}
