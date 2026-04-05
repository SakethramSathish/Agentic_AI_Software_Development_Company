import { Sun, Moon, Building2 } from 'lucide-react'
import { useTheme } from '../../context/ThemeContext'
import { motion } from 'framer-motion'

/**
 * Neo-Brutalist Navbar — thick bottom border, bold logo, theme toggle.
 */
export default function Navbar() {
  const { theme, toggleTheme } = useTheme()

  return (
    <nav
      className="sticky top-0 z-40 border-b-[3px] border-[var(--border-color)] px-6 py-4"
      style={{ background: 'var(--bg-primary)' }}
    >
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        {/* Logo */}
        <div className="flex items-center gap-3">
          <div className="bg-brutal-yellow border-[3px] border-[var(--border-color)] p-2"
               style={{ boxShadow: '3px 3px 0px 0px var(--shadow-color)' }}>
            <Building2 size={22} className="text-black" />
          </div>
          <div>
            <h1 className="font-heading text-lg font-extrabold tracking-tight" style={{ color: 'var(--text-primary)' }}>
              AGENTIC AI
            </h1>
            <p className="text-[0.65rem] font-heading font-bold uppercase tracking-[0.2em]" style={{ color: 'var(--text-secondary)' }}>
              Software Company
            </p>
          </div>
        </div>

        {/* Theme Toggle */}
        <motion.button
          whileHover={{ x: -2, y: -2 }}
          whileTap={{ x: 2, y: 2 }}
          onClick={toggleTheme}
          className="brutal-btn bg-brutal-purple text-white px-3 py-2 text-sm"
        >
          {theme === 'light' ? <Moon size={16} /> : <Sun size={16} />}
          <span className="hidden sm:inline">{theme === 'light' ? 'Dark' : 'Light'}</span>
        </motion.button>
      </div>
    </nav>
  )
}
