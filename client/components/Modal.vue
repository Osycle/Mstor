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
            <div class="tags-append">
              <tags-input element-id="tags"
                v-model="selectedTags"
                :input-id="'add-tags-input'"
                :existing-tags="[

                ]"
                placeholder="Добавить категорию"
                :discard-search-text="'Отменить результаты поиска'"
                :id-field="'value'"
                
                :typeahead="true"
                :typeahead-hide-discard="false"
                ></tags-input>
              </div>
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
  import { TagsInput } from '@seriouslag/vue-tagsinput';
  export default {
    props: ['modal-data', 'modal-manager'],
    data(){
      return {
        selectedTags: null,
        title: "",
        description: "",
        tags: [],
        ext: [
          { key: 'asd', value: 'Web Development' },
          { key: 'olo', value: 'PHP' },
          { key: 'javascript', value: 'JavaScript' },
        ]
      }
    },
    watch: {
      selectedTags(items){
        this.tags = []
        items.forEach(item => {
          this.tags.push(item.value)
          //console.log(item);
        });
        //this.tags
        //console.log(s, 11111111);
      }
    },
    computed: {
    },
    components: {
        TagsInput,
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
    background-color: rgba(black, 0.8);
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
    padding: 0;
  }
  .modal-header{
    position: relative;
    height: 35px;
    display: flex;
    color: white;
  }
  .modal-content{
    //padding: 20px;
    margin: auto;
    .text-content{
      display: flex;
      position: relative;
    }
    textarea{
      width: calc(100% - 40px);
      min-height: 200px;
      //border: 1px solid var(--color-1);
      border: 0;
      resize: none;
      background: var(--color-gray-2);
      padding: 20px 20px;
    }
  }
  .modal-footer{
    position: relative;
    height: 45px;
    pointer-events: none;
    *{
      pointer-events: auto;
    }
    .btn-content{
      height: auto;
      align-self: center;
      justify-self: right;
      margin-right: 0;
    }
  }

  .cap{
    @include shadow-border();
    align-self: center;
    padding: 5px 20px;
    background-color: $color-1;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    top: -17px;
  }
  .cap-btn-close{
    position: absolute;
    right: -65px;
    top: -10px;
    width: 40px;
    height: 100%;
    //border-left: var(--border-def);
    background-color: var(--color-3);
    @include hover-outshadow();
    span{
      width: 100%;
      height: 100%;
      position: relative;
      display: inline-block;
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
  .btn-def{
    position: absolute;
    right: -65px;
    bottom: -30px;
    height: 40px;
    background-color: var(--color-3);
    color: var(--color-1);
    padding: 10px 20px;
    font-weight: 600;
    //border-left: var(--border-def);
    @include hover-outshadow();
  }
</style>

