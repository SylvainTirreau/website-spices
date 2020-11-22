"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var build_blends_data_1 = require("./build-blends-data");
console.log(build_blends_data_1.data);
var BuildBlends = /** @class */ (function () {
    function BuildBlends() {
        this.flavors = build_blends_data_1.data.flavors;
        this.spices = build_blends_data_1.data.spices;
        this.compounds = build_blends_data_1.data.compounds;
    }
    BuildBlends.prototype.computeSpices = function (list) {
        // On doit détecter les doublons : si une épice a deux composées qui se retrouvent dans d'autres épices,
        // on doit les retrouver en premier. Voir comment on classe les épices au final, car une épise peut aussi se
        // retrouver dans plusieurs groupes.
    };
    return BuildBlends;
}());
