<template>
  <header id="header" class="header">
    <div class="header-wrapper">
      <div class="header-content">
        <!-- <nuxt-link to="/test" style="color: white;">Тест</nuxt-link> -->
        <div class="panel-top">
          <div class="panel-user">
            <div class="img-content">
              <img src="/img/user/avatar.jpg" alt="">
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>


<script>


export default {
  data(){
    return {

    }
  },

  async mounted(){

    
  }
}
</script>


<style lang="scss">
  .header{
    overflow: hidden;
    .header-wrapper{
      height: 40px;
      padding-left: 60px;
      padding-right: 60px;
      width: 100%;
      background-color: $color-1;
      // align-items: center;
      // justify-content: center;
      // box-shadow: 0px 8px 3px -4px rgba(black, 0.2);
    }
  }

  .panel-user{
    .img-content{
      display: flex;
      align-items: center;
    }
    img{
      border: 2px solid white;
      width: 30px;
      height: 30px;
      border-radius: 50%;
    }
  }

</style>