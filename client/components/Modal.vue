<template>
  <div>
    <div class="modal">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <div class="cap">
              Добавить
            </div>
            <span class="cap-btn-close">
              <span @click="$emit('modal-manager', 'close')"></span>
            </span>
          </div>
          <div class="modal-content">
            <div class="text-content">
              <textarea name="" id="" v-model="description"></textarea>
            </div>
            <!-- <tags-input element-id="tags"
                v-model="selectedTags"
                :existing-tags="[
                    { key: 'web-development', value: 'Web Development' },
                    { key: 'php', value: 'PHP' },
                    { key: 'javascript', value: 'JavaScript' },
                ]"
                :typeahead="true"></tags-input> -->
          </div>
          <div class="modal-footer">
            <div class="btn-content">
              <button type="button" class="btn-def" @click="addCell">
                <span>Сохранить</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

  export default {
    props: ['modal-data', 'modal-manager'],
    data(){
      return {
        selectedTags: null,
        title: "",
        description: "",
        tags: "",
      }
    },    
    computed: {
    },
    methods: {
      async addCell(){
        const response = await this.$axios.$post("/", {
          action: "insert",
          params: {
            title: this.title,
            description: this.description,
            tags: this.tags,
          }
        })
        if(response.status){
          this.$emit("append", response.cell)
          this.$emit("modal-manager", "close");
        }

        console.log(this.response);
      },
    },
    mounted(){
      console.log(this.modalData)
      console.log("Modal mounted")
    }
  }
</script>

<style lang="scss" scoped>
  .modal{
    position: fixed;
    width: 100%;
    height: 100%;
    background-color: rgba(black, 0.5);
    left: 0;
    top: 0;
    z-index: 100;
  }
  .modal-wrapper{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
  }
  .modal-container{
    width: 600px;
    background-color: white;
    padding: 0;
  }
  .modal-header{
    position: relative;
    height: 35px;
    display: flex;
    background-color: var(--color-1);
    color: white;
    border: var(--border-def);
  }
  .modal-content{
    //padding: 20px;
    margin: 0;
    .text-content{
      display: flex;
      border-left: var(--border-def);
      border-right: var(--border-def);
    }
    textarea{
      width: calc(100% - 40px);
      min-height: 200px;
      //border: 1px solid var(--color-1);
      border: 0;
      resize: none;
      background: var(--color-gray-2);
      padding: 20px 20px;
      &:focus{
        box-shadow: inset 0px 0px 1px 0px var(--color-3);
      }
    }
  }
  .modal-footer{
    height: 45px;
    background-color: var(--color-1);
    display: flex;
    justify-content: flex-end;
    border: var(--border-def);
    .btn-content{
      height: 100%;
      align-self: center;
      justify-self: right;
      margin-right: 0;
      .btn-def{
        height: 100%;
        background-color: var(--color-3);
        color: var(--color-1);
        padding: 10px 20px;
        font-weight: 600;
        border-left: var(--border-def);
        &:hover{
          box-shadow: inset -1px -1px 0px 0px black;
          animation: var(--animation-sir);
        }
      }
    }
  }
  .cap{
    align-self: center;
    padding: 5px 20px;
  }
  .cap-btn-close{
    position: absolute;
    right: 0;
    top: 0;
    width: 40px;
    height: 100%;
    border-left: var(--border-def);
    &:hover{
      cursor: pointer;
    }
    span{
      width: 100%;
      height: 100%;
      position: relative;
      display: inline-block;
      background-color: var(--color-3);
      &:hover{
        box-shadow: inset -1px -1px 0px 0px black;
        animation: var(--animation-sir);
      }
      &:before, &:after{
        content: "";
        display: inline-block;
        position: absolute;
        left: calc(50% - 10px);
        top: calc(50% - 1px);
        width: 20px;
        height: 2px;
        background-color: var(--color-1);
      }
      &:before{
        transform: rotate(45deg);
      }
      &:after{
        transform: rotate(-45deg);
      }
    }
  }

</style>