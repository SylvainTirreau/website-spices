import {data} from "./build-blends-data"

console.log(data)

class BuildBlends {
    flavors: object;
    spices: object;
    compounds: object;

    constructor() {
        this.flavors = data.flavors;
        this.spices = data.spices;
        this.compounds = data.compounds;
    }

    computeSpices(list) {
        // On doit détecter les doublons : si une épice a deux composées qui se retrouvent dans d'autres épices,
        // on doit les retrouver en premier. Voir comment on classe les épices au final, car une épise peut aussi se
        // retrouver dans plusieurs groupes.

    }

}

