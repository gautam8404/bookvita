import { writable } from "svelte/store";

export const loadingBarStore = writable(false);

export const setloadingBarStore = (value: boolean) => {
  loadingBarStore.set(value);
}

export const loadvalueStore = writable(0);

export const setloadvalue = (value: number) => {
  loadvalueStore.set(value);
}

export const updateLoadvalue = (value: number) => {
  loadvalueStore.update((n) => n + value);
}


