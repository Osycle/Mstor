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
    '@/static/scss/main.scss'
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://go.nuxtjs.dev/pwa
    '@nuxtjs/pwa',
    '@nuxtjs/axios',
    '@nuxt/http',
  ],
  // axios: {
  //   //baseURL: 'https://lada.uz/temp-api/',
  //   baseURL: 'http://mstor.server',
  //   //baseURL: 'https://html.lifestyle.uz/kia-api/',
  //   //baseURL: 'http://kia-api-php/',
  //   //withCredentials: true,
  //   headers: {
  //     Accept: 'application/x-www-form-urlencoded',
  //     'Content-Type': 'application/x-www-form-urlencoded'
  //   }
  // },
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
