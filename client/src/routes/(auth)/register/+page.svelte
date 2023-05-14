<script lang="ts">
	import type { PageData } from './$types';
	import { superForm } from 'sveltekit-superforms/client';
    import SuperDebug from "sveltekit-superforms/client/SuperDebug.svelte";

	export let data: PageData;
	const { form, errors, constraints } = superForm(data.form);
</script>

<SuperDebug data={$form} />

<div class="form-group bg-gray-500 p-8 text-black">
    <form method="POST">
        <div class="form-item">
            <label for="username">Username</label>
            <input type="text"
                   id="username"
                   name="username"
                   bind:value={$form.username}
                   data-invalid={$errors.username}
                   {...$constraints.username}
                   required
            />
            {#if $errors.username}<span class="invalid">{$errors.username}</span>{/if}
        </div>

        <div class="form-item">
            <label for="password">Password</label>
            <input type="password"
                   id="password"
                   name="password"
                   bind:value={$form.password}
                   data-invalid={$errors.password}
                   {...$constraints.password}
                   required
            />
            {#if $errors.password}<span class="invalid">{$errors.password}</span>{/if}
        </div>

        <div class="form-item">
            <label for="confirm_password">Confirm Password</label>
            <input type="password"
                   id="confirm_password"
                   name="confirm_password"
                   bind:value={$form.confirm_password}
                   data-invalid={$errors.confirm_password}
                   {...$constraints.confirm_password}
                   required
            />
            {#if $errors.confirm_password}<span class="invalid">{$errors.confirm_password}</span>{/if}
        </div>

        <div class="form-item">
            <label for="email">Email</label>
            <input type="email"
                   id="email"
                   name="email"
                   bind:value={$form.email}
                   data-invalid={$errors.email}
                   {...$constraints.email}
                   required
            />
            {#if $errors.email}<span class="invalid">{$errors.email}</span>{/if}

        </div>

        <div class="form-item">
            <label for="first_name">First Name</label>
            <input type="text"
                   id="first_name"
                   name="first_name"
                   bind:value={$form.first_name}
                   data-invalid={$errors.first_name}
                   {...$constraints.first_name}
                   required
            />
            {#if $errors.first_name}<span class="invalid">{$errors.first_name}</span>{/if}
        </div>

        <div class="form-item">
            <label for="last_name">Last Name</label>
            <input type="text"
                   id="last_name"
                   name="last_name"
                   bind:value={$form.last_name}
                   data-invalid={$errors.last_name}
                   {...$constraints.last_name}
                   required
            />
            {#if $errors.last_name}<span class="invalid">{$errors.last_name}</span>{/if}
        </div>

        <div class="form-item">
            <label for="profile_picture">Profile Picture</label>
            <input type="file"
                   id="profile_picture"
                   name="profile_picture"
                   accept="image/png, image/jpeg, image/gif, image/webp, image/jpg"
                   bind:value={$form.profile_picture}
                   data-invalid={$errors.profile_picture}
                   {...$constraints.profile_picture}
            />
            {#if $errors.profile_picture}<span class="invalid">{$errors.profile_picture}</span>{/if}
        </div>

        <div>
            <button type="submit">Submit</button>
        </div>

    </form>
</div>

<style>
    .form-item {
        @apply flex flex-col items-center justify-center w-2/4;
    }
    .invalid {
        @apply text-red-700;
    }
</style>