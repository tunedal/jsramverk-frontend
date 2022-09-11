import {Editor, Toolbar} from "./editor.js"

export default {
    data() {
        return {
            heading: "Henriks textredigerare",
        }
    },
    methods: {
        saveEditorContent() {
            this.$refs.editor.saveContent()
        }
    },
    components: {
        Editor,
        Toolbar,
    },
    template: "#app-template"
}
