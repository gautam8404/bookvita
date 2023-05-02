/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        'primary': '#FE7410',
        'secondary': '#A7A7A7'
      },
      fontFamily: {
        body: ['Poppins', 'sans-serif'],
      },
      content: {
        'search': 'url("/assets/search.svg")',
      },
      animation: {
        wiggle: 'wiggle 1s ease-in-out infinite',
      }
    },
  },
  plugins: [
    require('@tailwindcss/line-clamp'),
  ],
}

