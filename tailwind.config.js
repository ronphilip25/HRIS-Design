/** @type {import('tailwindcss').Config} */
module.exports = {
	content: [
		"**/templates/**/*.html"
	],
	theme: {      
		extend: {
			fontFamily: {
				sans: ['Inter', 'ui-sans-serif', 'system-ui'],
			  },
		},
	},
	plugins: [],
}