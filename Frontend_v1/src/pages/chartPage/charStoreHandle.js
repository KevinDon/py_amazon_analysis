const state = {
  //  本地配置
  localConfig: [2]
};

const getters = {
  getConfig: state => state.localConfig || null,
}

const mutations = {
  INIT_CONFIG: (state, payload) =>{
    state.localConfig = { ...payload
    }
  }
};

const actions = {
  init: (content, payload)=> {
    content.commit('INIT_CONFIG', payload);
  }
};

export default {
  state,
  getters,
  mutations,
  actions,
};
