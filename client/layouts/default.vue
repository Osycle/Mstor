<template>
  <div>
    <Header />
    <main id="main">
      <Nuxt />
    </main>
    <Footer />
  </div>
</template>


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
    }
  },
}


</script>
