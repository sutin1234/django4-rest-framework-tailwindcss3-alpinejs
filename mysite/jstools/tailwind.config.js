module.exports = {
   future: {
        removeDeprecatedGapUtilities: true,
        purgeLayersByDefault: true,
   },
    purge: {
       enabled: false, //true for production build
       content: [
         '../**/templates/*.html',
        '../**/templates/**/*.html'
       ]
   },
  theme: {
    extend: {
        fontFamily: {
            sans: ['Montserrat', 'Prompt', 'sans-serif']
        }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/aspect-ratio'),
  ],
}
