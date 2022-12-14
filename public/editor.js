export {Editor, Toolbar}

const Editor = {
    data() {
        return {}
    },
    methods: {
        saveContent() {
            let trix = this.$refs.trix.editor
            let content = trix.getDocument().toString()
            console.log(content)
        }
    },
    template: "#editor-template"
}

const Toolbar = {
    data() {
        return {}
    },
    methods: {
        save() {
            this.$emit("save")
        }
    },
    template: "#toolbar-template"
}
