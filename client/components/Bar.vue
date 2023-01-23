<template>
  <div>
    <div class="bar">
      <div class="bar-wrapper">
        <div class="bar-header">
        </div>
        <div class="bar-cap">
          <div class="cap">
            <span v-if="editable_cell">Редактировать</span>
            <span v-else>Добавить</span>
          </div>
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
        <div class="btn-content mv-3">
          <button type="button" class="btn-def" @click="submit" v-if="editable_cell && updated">
            <span class="this-btn">Сохранить</span>
          </button>
          <button type="button" class="btn-def" @click="submit" v-if="!editable_cell">
            <span class="this-btn">Добавить</span>
          </button>
        </div>
        <div class="bar-footer">
          <button type="button" class="btn-remove" @click="delCell(editable_cell)" v-if="editable_cell">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><path d="M24.2,12.193,23.8,24.3a3.988,3.988,0,0,1-4,3.857H12.2a3.988,3.988,0,0,1-4-3.853L7.8,12.193a1,1,0,0,1,2-.066l.4,12.11a2,2,0,0,0,2,1.923h7.6a2,2,0,0,0,2-1.927l.4-12.106a1,1,0,0,1,2,.066Zm1.323-4.029a1,1,0,0,1-1,1H7.478a1,1,0,0,1,0-2h3.1a1.276,1.276,0,0,0,1.273-1.148,2.991,2.991,0,0,1,2.984-2.694h2.33a2.991,2.991,0,0,1,2.984,2.694,1.276,1.276,0,0,0,1.273,1.148h3.1A1,1,0,0,1,25.522,8.164Zm-11.936-1h4.828a3.3,3.3,0,0,1-.255-.944,1,1,0,0,0-.994-.9h-2.33a1,1,0,0,0-.994.9A3.3,3.3,0,0,1,13.586,7.164Zm1.007,15.151V13.8a1,1,0,0,0-2,0v8.519a1,1,0,0,0,2,0Zm4.814,0V13.8a1,1,0,0,0-2,0v8.519a1,1,0,0,0,2,0Z"/></svg>
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
    props: ['current_cell'],
    data(){
      return {
        editable_cell: null,
        selectedTags: [],
        content: "",
        tags: [],
        existing_tags: [],
        customToolbar: [
          ["bold", "italic", "underline"],
          [{ list: "ordered" }, { list: "bullet" }],
          ["image", "code-block", "link"],
          ["clean"]
        ],
        editorOptions: {
          theme: 'snow',
          // debug: 'info',
          modules: {
            imageDrop: true,
            magicUrl: true,
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
      content(current_content, old_content){
        // z.match(/https?:\/\/.*?(?=\s|\n|<)/gim)
        // console.log(current_content, old_content)
      },
      current_cell(cell){
        console.log(cell)
        this.selectedTags = []
        this.editable_cell = cell
        if(cell){
          this.content = cell.content
          cell.tags.forEach((item)=>{
            this.selectedTags.push({value: item.name})
          })
        }else{
          this.clear()
        }

      },
    },
    computed: {
      updated(){
        let change_status = false, editable_tags = []
        this.editable_cell.tags.forEach(({name})=>{editable_tags.push(name)})
        if(this.editable_cell.content != this.content)
          change_status = true;
        if(!this.$_.isEqual(editable_tags, this.tags))
          change_status = true;
        return change_status
      }
    },
    components: {
      TagsInput,
    },
    async created(){
      const response = await this.$axios.$get("/tags/")
      this.all_tags = response.tags
      this.all_tags.forEach(item => {
        this.existing_tags.push({value: item.name})
      });
    },
    mounted(){
      // console.log(VueEditor) 
    },
    methods: {
      customModulesForEditor (d){
        console.log(d, "customModulesForEditor")
      },
      // text_change(delta, oldDelta, source){
      //   console.log(this);
      //   function isWhitespace(ch) {
      //     var whiteSpace = false
      //     if ((ch == ' ') || (ch == '\t') || (ch == '\n')) {
      //       whiteSpace = true;
      //     }
      //     return whiteSpace;
      //   }
      //   var regex = /https?:\/\/[^\s]+$/;
      //   if(delta.ops.length === 2 && delta.ops[0].retain && isWhitespace(delta.ops[1].insert)) {
      //     var endRetain = delta.ops[0].retain;
      //     var text = quill.getText().substr(0, endRetain);
      //     var match = text.match(regex);

      //     if(match !== null) {
      //       var url = match[0];

      //       var ops = [];
      //       if(endRetain > url.length) {
      //         ops.push({ retain: endRetain - url.length });
      //       }

      //       ops = ops.concat([
      //         { delete: url.length },
      //         { insert: url, attributes: { link: url } }
      //       ]);

      //       quill.updateContents({
      //         ops: ops
      //       });
      //     }
      //   }
      // },
      content_blur(quill){
        // const pattern_link = /((?<!<a.+)https?:\/\/.*?(?=[\s\n<'"]))/gim;
        const pattern_link = /((?<!<a.+)https?:\/\/.*?(?=[\s\n<'"])|(?<=<\/a>.+)https?:\/\/.*?(?=[\s\n<'"]))/gim;
        // this.content.replace()
        
        // this.content = this.content.replace("</p>", "</p>\n");
        this.content = this.content.replace(pattern_link, "<a href=\"$1\" rel=\"noopener noreferrer\" target=\"_blank\">$1</a>");
        // console.log(this.content)
        console.log(this.content, quill)
      },
      clear(){
        this.editable_cell = null
        this.content = ""
        this.selectedTags = []
      },
      async submit(){
        if(this.editable_cell)
          this.editCell()
        else
          this.addCell()
      },
      async editCell(){
        const response = await this.$axios.$put("/cells/"+this.editable_cell.id+"/", {
          content: this.content,
          tags: this.tags
        })
        if(response.status){
          this.$emit("cell_update", response.cell)
        }
      },
      async addCell(){
        const response = await this.$axios.$post("/cells/", {
          content: this.content,
          tags: this.tags
        })
        if(response.status){
          this.$emit("cell_append", response.cell)
          this.editable_cell = response.cell
          console.log(this.current_cell, 'this.current_cell');
        }
      },
      async delCell(cell){
        const response = await this.$axios.$delete("/cells/"+cell.id+"/")
        if(response.status){
          this.$emit("cell_remove", cell.id)
          this.clear()
        }
      },
    },
  }
</script>

<style lang="scss">

</style>

<style lang="scss" scoped>


</style>

