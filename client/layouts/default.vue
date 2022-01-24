<template>
  <div>
    <Header />
    <main id="main">
      <Nuxt />
    </main>
    <Footer />
  </div>
</template>

<style lans="scss">
  /* @import "~vue-wysiwyg/dist/vueWysiwyg.css"; */
  
</style>
<script>
  
import Header from '@/components/Header'
import Footer from '@/components/Footer'

export default {
  components: {
    Header,
    Footer
  },
  head() {
    return {
      script: [
        {src: '/js/plugins/jquery.min.js'},
        {src: '/js/plugins/jquery.fancybox.js'},
      ],
      link: [
        {href: '/fonts/MyriadPro/stylesheet.css'},
        // {href: '@/node_modules/vue-wysiwyg/dist/vueWysiwyg.css'}
      ]
    }
  },
}


</script>
