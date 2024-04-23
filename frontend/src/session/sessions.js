// this is insanely unbelievably insecure
// in the real world, if an employer catches you doing this you'll be fired instantly
// then thrown into a volcano

import { reactive } from '@vue/reactivity'
import { nextTick } from 'vue'


import router from "../router/index.js"

export const sess = reactive({
    logged_in: false
});

export function startSession(username) {
    // we're not even going to bother with timing out :D why not
    sessionStorage.setItem("session", username)
    sess.logged_in = true
}

export function getSession() {
    const s = sessionStorage.getItem("session");
    if (sess.logged_in && s === null) {
        sess.logged_in = false
        nextTick(() => router.push("home"));
    } else if (!sess.logged_in && s !== null) {
        sess.logged_in = true
    }
    return s
}

export function sessionExists() {
    return getSession() !== null;
}

export function endSession() {
    sessionStorage.removeItem("session")
    sess.logged_in = false
}

export default {startSession, getSession, sessionExists, endSession, sess};