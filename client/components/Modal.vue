<template>
  <div>
    <div class="modal">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <div class="cap">
              <span v-if="edit_cell">Редактировать</span>
              <span v-else>Добавить</span>
            </div>
            <span class="cap-btn-close">
              <span @click="$store.commit('modal/close')"></span>
            </span>
          </div>
          <div class="modal-content">
            <div class="text-content">
              <client-only>
                <!-- 
                  :editor-toolbar="customToolbar" 
                  :customModules="customModulesForEditor"
                  :editorOptions="editorSettings"
                -->
                <VueEditor
                  v-model="content" 
                  :editorOptions="editorSettings"
                  />
                <!-- <textarea v-else v-model="content"></textarea> -->
              </client-only>
            </div>
            <div class="tags-append">
              <tags-input element-id="tags"
                v-model="selectedTags"
                :input-id="'add-tags-input'"
                :existing-tags="existing_tags"
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
              <button type="button" class="btn-def" @click="submit">
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
    props: ['all_tags'],
    data(){
      return {
        selectedTags: [],
        content: "",
        tags: [],
        existing_tags: [],
        customToolbar: [
          ["bold", "italic", "underline"],
          [{ list: "ordered" }, { list: "bullet" }],
          ["image", "code-block"]
        ],
        editorSettings: {
          modules: {
            imageDrop: true,
            imageResize: {}
          }
        }
      }
    },
    watch: {
      selectedTags(items){
        this.tags = []
        items.forEach(item => {
          this.tags.push(item.value)
        });
      },
      description(a, s, r){
        // console.log(a, s, r)
      }
    },
    computed: {
      edit_cell(){
        return this.$store.state.modal.edit_cell
      }
    },
    components: {
      TagsInput,
    },
    created(){
      if(this.edit_cell){
        this.content = this.edit_cell.content
        this.edit_cell.tags.forEach((item)=>{
          this.selectedTags.push({value: item.name})
        })
      }
      this.all_tags.forEach(item => {
        this.existing_tags.push({value: item.name})
      });
      // console.log(this.edit_cell);
    },
    mounted(){
      window.ss = this
      // console.log(this.all_tags)
    },
    methods: {
      customModulesForEditor (d){
        console.log(d, "customModulesForEditor")
      },
      async submit(){
        if(this.edit_cell)
          this.editCell()
        else
          this.addCell()
      },
      async editCell(){
        const response = await this.$axios.$put("/cells/"+this.edit_cell.id+"/", {
          action: "edit_cell",
          content: this.content,
          tags: this.tags
        })
        if(response.status){
          this.$emit("cell_update", response.cell)
          this.$store.commit("modal/close")
        }
      },
      async addCell(){
        const response = await this.$axios.$post("/cells/", {
          action: "add_cell",
          content: this.content,
          tags: this.tags
        })
        if(response.status){
          this.$emit("cell_append", response.cell)
          this.$store.commit("modal/close")
        }
      },
    },
  }
</script>

<style lang="scss">
  .ql-toolbar{
    background-color: white;
  }
  .modal-content .ql-editor{
    background-color: white;
    color: black;
    overflow-y: auto;
    height: calc(100vh - 330px);
  }
  .ql-container{
    
    // max-height: calc(100vh - 300px);
  }
</style>

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
    // width: calc(100% - 330px);
    max-width: 75%;
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
      position: relative;
    }
    textarea{
      width: 800px;
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

