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
            "js/constants",
            "MP",
            "js/crud",
            "view/document",
        ],
        function (Const, MP, Crud, Doc) {
       
    function handleSubmit(gameParams) {
        gameParams = readyGameForSubmit(gameParams);

        Crud.createGame(gameParams, this);
        var docView = Doc.retrieve();
        docView.hideDialog();
    }
    
    function handleSuccess(numberOfTags) {
        MP.trackCreateGame(
                numberOfTags,
                null,
                null);
        // refresh the Docview with by grabbing new data
        var docView = Doc.retrieve();
        docView.refresh();
    }

    function readyGameForSubmit(gameParams) {
        // for each player, if no score then append score 0.
        var gamescore = gameParams[Const.DATA.GAME_SCORE];
        var i;
        var player;
        for (i = 0; i < gamescore.length; i += 1) {
            player = gamescore[i];
            if (!player.hasOwnProperty(Const.DATA.SCORE)) {
                player[Const.DATA.SCORE] = 0;
            }
        }

        return gameParams;
    }
    
    return {
        handleSubmit: handleSubmit,
        handleSuccess: handleSuccess,
    };
});
