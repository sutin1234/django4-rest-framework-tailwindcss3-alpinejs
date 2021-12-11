module.exports = {
  plugins: {
    require('postcss-import'),
    require('tailwindcss'),
    require('autoprefixer'),
    ...(NODE_ENV === 'production' ? { cssnano: {} } : {})
  },
}
