/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			colors: {
				primary: '#FE7410',
				secondary: '#A7A7A7'
			},
			fontFamily: {
				body: ['Poppins', 'sans-serif']
			}
		}
	},
	plugins: [
		require('@tailwindcss/line-clamp'),
		...(process.env.NODE_ENV === 'production' ? [require('cssnano')] : [])
	]
};
