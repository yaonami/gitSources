function emoji(red,green,blue){

    emojiColors = ['#859fb8', '#819cb6', '#7b98b4', '#7f9bb6', '#7e9ab4', '#7e9ab5', '#7e9ab5', '#819cb6', '#7a97b2', '#809cb6', '#7f9ab5', '#313131', '#313131', '#c9291a', '#c72b1c', '#353535', '#819ab1', '#89a0b5', '#88a0b5', '#88a1ba', '#88a1b9', '#87a1ba', '#87a1b9', '#869eb4', '#859db3', '#878787', 'false', '#8ba4bc', '#86a1ba', '#889fb5', '#8da3b8', 'false', 'false', '#3eabd0', '#343434', '#cfcfcf', '#849fb8', '#819cb6', '#cfcfcf', '#333333', '#cacaca', '#383838', '#eba52c', '#bfc3cf', '#a72c31', '#6f6f6f', 'false', 'false', '#ba8d6a', '#dea635', '#a55ebc', '#a45fbb', '#a764bd', '#a05cb8', '#a561bb', '#a764bd', '#aa68bf', '#a862be', '#a35dba', '#a764bd', '#a664bc', '#a660bd', '#2d2d2d', '#282828', '#d45d4e', '#c84838', '#cb2d1d', '#2d8e3a', '#367ddc', '#45607d', '#cfb235', '#efa631', '#cacaca', '#474747', 'false', 'false', '#8b878c', '#d9c4a3', '#a865be', 'false', '#83776c', 'false', '#6a7014', 'false', 'false', '#7e3524', 'false', '#31b836', 'false', '#c8c8c8', '#c39875', '#c3a080', '#bb906d', 'false', 'false', '#212121', '#262626', '#eaa41a', '#39b351', '#f19b49', '#a6c1e2', '#39b551', '#cf2b1b', '#45bb4a', '#d53020', '#c6c6c6', '#b9b9b9', '#c92919', '#ca4535', '#262626', '#252525', '#262626', '#89a2bb', '#292929', '#3393dd', '#8099b1', '#819ab1', '#86a0b9', '#849eb7', '#87a1b9', '#333333', '#e0e0e0', '#deb967', '#ca2a1a', '#272727', '#cc971c', '#db5542', '#da5a48', 'false', '#c6a48f', '#a19b98', '#d04b3c', '#d15243', '#d14e3f', '#337edd', '#d35e50', '#cb4c42', '#829db7', '#859db4', '#a677c1', '#88a1b9', '#809ab4', '#809bb5', '#ca4b40', '#849cb3', '#f19842', '#d83c16', 'false', 'false', 'false', 'false', 'false', '#dab0ac', '#a79ea4', 'false', 'false', '#849eb8', '#347edd', '#f19e52', '#41b758', '#d45849', '#6954bd', '#d75544', '#e26856', '#f29c4e', '#f39b48', '#f29d4c', '#db6595', '#f29d4f', '#db0000', '#cb8943', '#175cda', '#adbec3', '#b73b57', 'false', 'false', 'false', 'false', 'false', 'false', 'false', '#4d5e7b', 'false', 'false', 'false', 'false', 'false', '#6386a3', '#494c5a', '#6d6a60', 'false', 'false', '#e8d476', 'false', 'false', 'false', '#e9be4b', '#606372', '#d4b955', '#d5ba56', '#ddc458', '#daa02b', 'false', 'false', 'false', '#2e8818', '#5b680f', '#637312', '#457b2b', '#3f7e2a', 'false', '#c88d95', '#9c3415', 'false', 'false', '#c09422', 'false', '#54732a', 'false', '#3ca32b', 'false', 'false', '#639328', 'false', 'false', 'false', 'false', 'false', '#c27165', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', '#9d652e', 'false', 'false', '#946141', 'false', '#848678', '#bfbfbf', 'false', 'false', 'false', 'false', 'false', '#8d634d', 'false', 'false', '#ae4133', 'false', '#dfc9d5', 'false', 'false', '#bcb3a6', '#5e3413', 'false', 'false', 'false', 'false', 'false', 'false', '#c49583', 'false', 'false', '#524e40', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', '#c0c6b0', '#b84281', 'false', '#c4afac', '#b56a15', '#63741c', 'false', 'false', 'false', '#b4333c', 'false', 'false', 'false', '#ab9693', 'false', 'false', 'false', '#7a9ab1', 'false', '#88202c', '#3e3933', 'false', 'false', '#9e8d92', 'false', 'false', '#262626', '#8ca4bb', 'false', 'false', 'false', 'false', '#aaa566', 'false', 'false', '#3e3e3f', 'false', 'false', '#414141', '#c0bebe', 'false', '#628565', '#7977c4', '#171717', 'false', '#8d4c20', '#8f8f91', 'false', 'false', '#232323', '#4daada', 'false', '#17b290', 'false', 'false', '#b1a999', 'false', 'false', 'false', 'false', 'false', 'false', '#3f9fa0', '#8d866e', 'false', '#9fa6ad', '#998e7e', 'false', '#9a8d8e', '#718487', 'false', '#907774', '#9a6d85', 'false', '#9c965b', '#8e9199', 'false', 'false', '#8aa49b', 'false', '#938986', '#d8cac9', '#a26d3a', '#453d3e', '#7d7774', 'false', 'false', '#d2c9c7', 'false', '#447d4e', '#5f8159', '#7f92aa', 'false', '#017633', '#4a3f15', '#c4bd9d', '#cac7b4', '#a7997c', '#665335', '#cdaaa1', '#b38b78', '#be9860', '#d2a685', 'false', '#867a7e', '#884147', '#ab9e9c', 'false', '#242423', 'false', 'false', 'false', 'false', 'false', '#447536', 'false', 'false', 'false', 'false', 'false', 'false', 'false', '#b58a52', 'false', '#157a82', '#9d9194', 'false', '#987c30', '#897f81', '#b39338', '#497547', '#35708d', '#675735', 'false', 'false', '#b7848e', '#176a30', 'false', 'false', '#8f6e33', '#868685', '#b96e81', '#c32226', '#9f9d98', '#c7a080', '#c9a07e', 'false', '#9f6573', '#bf9e7f', '#c8a586', '#c2a081', '#c2a082', '#c39a78', '#bc9d80', '#bd9473', '#c29876', '#c69d7c', '#c49872', '#c19f80', 'false', 'false', '#5d6368', 'false', '#5a6f91', '#38437b', '#0f8e81', '#ac6e23', '#c85873', '#9a5f82', '#bf6a8e', 'false', '#c69c66', '#452e26', '#9a9998', 'false', '#a59069', 'false', '#b01b1e', '#576e88', '#4b5f78', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', '#a9876c', 'false', 'false', '#7b3523', 'false', 'false', 'false', '#687374', '#67557e', 'false', 'false', 'false', '#463d33', '#942217', 'false', '#c2858c', 'false', 'false', 'false', 'false', 'false', '#c3123b', '#cca39b', 'false', '#7abfe7', 'false', 'false', 'false', '#8b6769', 'false', '#c43b2a', 'false', 'false', '#ce4893', 'false', '#2e7edf', 'false', '#eabe4e', 'false', 'false', 'false', '#dc77ca', 'false', '#bfb499', '#b52618', 'false', '#002f7f', '#f47845', 'false', 'false', '#a6b7d5', '#7e5a3a', '#c39874', '#cab160', '#cacaca', '#dddddd', '#bc2210', '#c40000', 'false', '#2b2b2b', '#161616', '#a59f88', 'false', '#9c9782', 'false', 'false', 'false', '#31b54b', 'false', 'false', '#64524f', 'false', '#86898c', '#c7c7c1', '#d0c49d', '#a5adb5', '#98a2aa', '#d4d4d4', '#d9d9d9', '#bd9999', 'false', '#979696', '#d2ccd0', '#c7d0de', '#b7bfc5', '#bda994', '#9d261c', '#a8312d', '#898989', '#758198', '#8993a9', '#ced1d5', '#c6af2f', 'false', '#bb9a60', '#8d2d2b', '#808f9b', '#658537', '#316388', '#b67327', 'false', 'false', '#c8ae8f', '#beb4a4', '#464646', 'false', '#b0ac9a', 'false', 'false', 'false', '#bba8b1', '#bba4ab', '#99754c', '#a9b0cb', '#c7bfbe', '#c9b5b0', 'false', 'false', 'false', 'false', '#9f3e2f', 'false', '#b2b2b1', '#474949', '#3e4c56', '#f19949', '#f2a151', 'false', '#88a2bb', 'false', 'false', 'false', 'false', '#4b4d52', '#86a1bb', '#88a3bd', '#89a3bc', '#212121', '#89a2bc', '#dfb041', '#e5b544', 'false', 'false', 'false', 'false', 'false', '#302f2a', 'false', 'false', 'false', 'false', '#b77931', 'false', 'false', 'false', 'false', '#c09993', '#787878', 'false', '#282828', '#272727', '#292929', '#292929', '#262626', 'false', '#8aa1b6', '#859db3', '#829ab1', '#7f98b0', '#849db3', '#7f98b0', '#e3992c', '#737b85', '#9fa1a4', 'false', '#6d6d6d', '#868686', 'false', 'false', '#909192', 'false', '#a263b8', 'false', '#cbb23c', '#606060', '#919191', 'false', 'false', '#e8953b', '#3a73e3', 'false', '#3469cf', 'false', 'false', '#869eb4', '#879eb4', '#c4c4c4', '#c4c4c4', '#c4c4c4', '#c4c4c4', '#c4c4c4', '#c4c4c4', '#c4c4c4', '#c4c4c4', '#c4c4c4', '#c4c4c4', '#c4c4c4', '#c5c5c5', '#c3c3c3', '#c4c4c4', '#c4c4c4', '#c4c4c4', '#c4c4c4', '#c5c5c5', '#c4c4c4', '#c3c3c3', '#c4c4c4', '#c3c3c3', '#c5c5c5', '#c3c3c3', 'false', '#b6a8ad', 'false', '#638cb5', '#747474', '#ce9c3a', '#d2a347', 'false', '#cc9938', '#cc9939', 'false', 'false', '#be9e48', 'false', '#ddab37', '#dda334', '#daa53c', '#dfac36', '#d68c2e', '#a68333', '#dbaa37', '#e1ac37', '#e5b13a', '#dcaa37', '#cfab46', '#dca936', '#e3af38', '#d2a033', '#e4af38', '#d79932', '#e1ad37', '#dea534', '#d89d3e', 'false', '#d4993c', '#e0ad38', '#dca835', '#dca837', '#c4591d', '#d5aa42', '#d8a635', '#dab14f', '#d6ab41', '#deaa37', '#d8a534', 'false', '#cb9934', '#cca03f', '#cc9a34', '#d5a548', 'false', '#e4af39', '#dca936', 'false', 'false', '#d1a034', 'false', '#cea33d', '#cd9a30', '#e7b239', 'false', '#a28534', 'false', '#a78935', '#aa7b2c', '#b29131', '#b78e2f', '#b79533', '#ac913b', '#a98d3b', 'false', 'false', 'false', 'false', '#8d744d', 'false', 'false', '#b39d83', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', '#7f88b0', 'false', '#525959', 'false', '#575853', '#4f5553', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', 'false', '#346387', 'false', '#2e614e', 'false', 'false', 'false', 'false', 'false', '#5f5c43', 'false', 'false', 'false', 'false', '#5b574e', 'false', 'false', '#cb5640', '#a3723d', '#c6291a', 'false', '#3b82dd', '#7d97b2', 'false', '#3077d8', 'false', 'false', 'false', 'false', 'false', 'false', 'false', '#97850b', '#2d79db', '#d964c3', '#89a2bb', '#f29c4c', '#a5a5a5', '#3b83de', 'false', 'false', '#878787', '#347bd9', '#387cd9', '#4989dc', '#3e81db'];

    emojiInts = emojiPoints();
    emojiMap = loadEmojis();

    function closeEmoji(red,green,blue){
        var distance = 99999999;
        var c, d, p;
        for (let i=0; i<emojiInts.length; i++){
            p = emojiInts[i];
            d = Math.sqrt( Math.pow((red-p[0]), 2) + Math.pow((green-p[1]), 2) + Math.pow((blue-p[2]), 2) );
            if (d < distance){
                distance = d;
                c = p[3];
            }
        }
        return emojiMap[c];
    }

    return closeEmoji(red,green,blue);

    function loadEmojis(){
        var colorMap = {};
        for (var i=0; i<emojiColors.length; i++){
            if ( emojiColors[i] == 'false' ) {
                continue;
            }
            fileNumber = pad(i+1 , 4);
            img = 'resized-emoji-images/' + fileNumber + '.png';
            colorMap[emojiColors[i]] = img
        }
        return colorMap;
    }

    function pad(num, size){
        return ('000' + num).substr(-size);
    }

    function emojiPoints(){
        var pointArray = [];
        var c, r, g, b;
        for (var i=0; i<emojiColors.length; i++){
            c = emojiColors[i];
            r = parseInt("0x"+c.substr(1,2));
            g = parseInt("0x"+c.substr(3,2));
            b = parseInt("0x"+c.substr(5,2));
            pointArray.push([r, g, b, c]);
        }
        return pointArray;
    }
}
