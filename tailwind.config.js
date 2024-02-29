/** @type {import('tailwindcss').Config} */
module.exports = {
	content: [
		"**/templates/**/*.html"
	],
	theme: {
        fontFamily: {
			'sans': ['Inter', 'sans-serif'],
			'serif': ['Inter', 'serif'],
			'mono': ['Inter', 'monospace'],
		  },      
		extend: {},
	},
	plugins: [],
}