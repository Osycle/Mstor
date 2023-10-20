export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  target: 'server',
  // mode: 'spa',
  ssr: true,
  server: {
    port: 3030,
  },
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
    { src: '~/plugins/owl.js', ssr: false },
    { src: '~/plugins/vue2-masonry-wall.js', srr: false },
    { src: '~/plugins/vue2-editor.js', ssr: false },
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
    "vue2-editor/nuxt",
  ],
  axios: {
    // baseURL: 'http://localhost:4040/cgi-bin/',
    // baseURL: 'http://127.0.0.1:8000/api/v1/',
    baseURL: 'http://localhost:8000/api/v1/',
    //credentials: false,
    headers: {
      //"Content-Type": "application/json; charset=UTF-8",
      //"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
      // "Accept": "*/*",
      //"Allow": "CONVERT",
      //"IOsycle": "IO",
      // "Access-Control-Allow-Origin": "*",
      //"Access-Control-Request-Headers": "Content-Type" ,
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
