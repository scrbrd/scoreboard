/* 
    Module: controller/createGame
    Handle tab updating by a returning a stateless object.

    Dependencies:
        MP
        crud
        view/document
*/
define(
        [
            "MP",
            "js/crud",
            "view/document",
        ],
        function (MP, Crud, Doc) {
       
    function handleSubmit(gameParams) {
        Crud.createGame(gameParams, this);
        var docView = Doc.retrieve();
        docView.hideDialog();
    }
    
    function handleSuccess(numberOfTags) {
        MP.trackCreateGame(
                numberOfTags,
                null,
                null);
        var docView = Doc.retrieve();
        // TODO: refresh the Docview with by grabbing new data
        //docView.refresh();
    }
    
    return {
        handleSubmit: handleSubmit,
        handleSuccess: handleSuccess,
    };
});
