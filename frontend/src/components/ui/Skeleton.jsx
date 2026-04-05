/**
 * Neo-Brutalist skeleton loader — solid color block with pulse.
 */
export default function Skeleton({ className = '', width = '100%', height = '1rem' }) {
  return (
    <div
      className={`animate-pulse border-[3px] border-[var(--border-color)] ${className}`}
      style={{
        width,
        height,
        background: 'var(--bg-secondary)',
      }}
    />
  )
}
