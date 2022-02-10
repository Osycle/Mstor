export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'mstor',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
  server: {
    port: 5000,
  },
  loading: { color: '#05141F' },
  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '@fancyapps/ui/dist/fancybox.css',
    '@assets/scss/_common.scss',
    '@assets/scss/main.scss'
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    // { src: '~plugins/nuxt-quill-plugin', ssr: false }
    { src: '~/plugins/lodash.js' },
    { src: '~/plugins/vue-tagsinput.js' },
    { src: '~/plugins/vue-filter-date-format.js' },
  ],
  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    '@nuxtjs/style-resources',
  ],
  styleResources: {
    scss: '@assets/scss/_variables.scss'
  },
  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    '@nuxtjs/axios',
    '@nuxt/http',
  ],
  axios: {
    baseURL: 'http://mstor.server',
    withCredentials: true,
    headers: {
      //Accept: "*/*",
      //"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
  },
  // PWA module configuration: https://go.nuxtjs.dev/pwa
  pwa: {
    manifest: {
      lang: 'en'
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  }
}
