<template>
  <div>
    <div class="bar">
      <div class="bar-wrapper">
        <div class="bar-cap">
          <div class="cap">Добавить</div>
        </div>
        <div class="bar-input">
          <client-only>
            <VueEditor
              v-model="content" 
              :editorToolbar="customToolbar"    
              :editorOptions="editorOptions"
              />
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
        <div class="btn-content mt-3 flex jc-end">
          <button type="button" class="btn-def" @click="submit">
            <span>Сохранить</span>
          </button>
        </div>
        <div class="bar-footer mv-3">
          <button type="button" class="btn-def red-btn" @click="submit">
            <span>Удалить</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { TagsInput } from '@seriouslag/vue-tagsinput';


  export default {
    props: ['cur_cell'],
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
        editorOptions: {
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
      },
      cur_cell(cell){
        console.log(cell)
        this.selectedTags = []
        if(cell){
          this.content = cell.content
          cell.tags.forEach((item)=>{
            this.selectedTags.push({value: item.name})
          })
        }
      },
    },
    computed: {
      // edit_cell(){
      //   return this.$store.state.modal.edit_cell
      // }
    },
    components: {
      TagsInput,
    },
    async created(){
      this.edit_cell = this.cur_cell

      const response = await this.$axios.$get("/tags/")
      this.all_tags = response.tags
      this.all_tags.forEach(item => {
        this.existing_tags.push({value: item.name})
      });
      // console.log(this.edit_cell);
    },
    mounted(){
      // body
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
          content: this.content,
          tags: this.tags
        })
        if(response.status){
          // this.$emit("cell_update", response.cell)
          // this.$store.commit("modal/close")
        }
      },
      async addCell(){
        const response = await this.$axios.$post("/cells/", {
          content: this.content,
          tags: this.tags
        })
        if(response.status){
          // this.$emit("cell_append", response.cell)
          // this.$store.commit("modal/close")
        }
      },
    },
  }
</script>

<style lang="scss">

</style>

<style lang="scss" scoped>


</style>

