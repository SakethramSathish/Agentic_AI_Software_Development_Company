/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: ['class', '[data-theme="dark"]'],
  theme: {
    extend: {
      fontFamily: {
        heading: ['"Space Grotesk"', 'sans-serif'],
        body: ['"Inter"', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'monospace'],
      },
      colors: {
        brutal: {
          cream: '#FFFDF7',
          peach: '#FFF3E0',
          purple: '#A855F7',
          yellow: '#FACC15',
          pink: '#EC4899',
          blue: '#38BDF8',
          green: '#4ADE80',
          orange: '#FB923C',
          red: '#F87171',
          indigo: '#818CF8',
          teal: '#2DD4BF',
          amber: '#F59E0B',
        },
        dark: {
          900: '#2A1F2D',
          800: '#362A3A',
          700: '#3E3042',
          600: '#4A3B4E',
        },
      },
      boxShadow: {
        'brutal': '4px 4px 0px 0px #000000',
        'brutal-lg': '6px 6px 0px 0px #000000',
        'brutal-sm': '2px 2px 0px 0px #000000',
        'brutal-dark': '4px 4px 0px 0px rgba(255,255,255,0.15)',
        'brutal-dark-lg': '6px 6px 0px 0px rgba(255,255,255,0.15)',
        'brutal-dark-sm': '2px 2px 0px 0px rgba(255,255,255,0.15)',
      },
      animation: {
        'pulse-brutal': 'pulse-brutal 1.5s ease-in-out infinite',
        'slide-up': 'slide-up 0.4s ease-out',
        'slide-in-right': 'slide-in-right 0.3s ease-out',
      },
      keyframes: {
        'pulse-brutal': {
          '0%, 100%': { transform: 'scale(1)' },
          '50%': { transform: 'scale(1.05)' },
        },
        'slide-up': {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        'slide-in-right': {
          '0%': { opacity: '0', transform: 'translateX(20px)' },
          '100%': { opacity: '1', transform: 'translateX(0)' },
        },
      },
    },
  },
  plugins: [],
}
