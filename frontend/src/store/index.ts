import { createStore } from 'vuex';
import { auth } from '../firebase/config';
import {
    createUserWithEmailAndPassword,
    signInWithEmailAndPassword,
    signOut,
    GoogleAuthProvider,
    signInWithPopup
} from 'firebase/auth'


const init_state = {
    user: null,

};


const store = createStore({
    state: {
        //The user state will initially be null. After login, this state will be updated
        user: null
    },
    mutations: {
        //Mutation to update the user state
        //Takes in two arguments, the state and the payload. When we call this mutation, the payload will be user object from firebase auth
        //When the user logs out, we call the mutation and the payload will be null
        setUser(state, payload) {
            state.user = payload
            //Log out the user state
            console.log(state.user)
        }
    },
    actions: {
        async signup(context, { email, password }) {
            const response = await createUserWithEmailAndPassword(auth, email, password)
            if (response) {
                context.commit('setUser', response.user)
            } else {
                throw new Error('signup failed')
            }
        },

        async login(context, { email, password }) {
            const response = await signInWithEmailAndPassword(auth, email, password)
            if (response) {
                context.commit('setUser', response.user)
            } else {
                throw new Error('login failed')
            }
        },

        async logout(context) {
            await signOut(auth)

            context.commit('setUser', null)
        },

        async goolgeLogin(context) {
            const provider = new GoogleAuthProvider();
            const response = await signInWithPopup(auth, provider);
            if (response) {
                context.commit('setUser', response.user)
            }
        }
    }
})

// export the store
export default store