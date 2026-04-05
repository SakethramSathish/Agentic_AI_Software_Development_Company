import Navbar from './Navbar'

/**
 * Main layout wrapper — Navbar + content area.
 */
export default function Layout({ children }) {
  return (
    <div className="min-h-screen" style={{ background: 'var(--bg-primary)' }}>
      <Navbar />
      <main className="max-w-7xl mx-auto px-4 sm:px-6 py-8">
        {children}
      </main>
    </div>
  )
}
