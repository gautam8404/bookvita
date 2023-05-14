import type { PageServerLoad } from './$types';
import type { Actions } from './$types';

import { fail } from '@sveltejs/kit';
import { z } from 'zod';
import { superValidate } from 'sveltekit-superforms/server';

const MAX_FILE_SIZE = 1024 * 1024; // 1MB
const ALLOWED_MIME_TYPES = ['image/jpeg', 'image/png', 'image/jpg', 'image/gif'];

const registerSchema = z
	.object({
		username: z.string().min(3).max(20),
		email: z.string().email().max(255),
		password: z
			.string()
			.min(8)
			.max(50)
			.refine((password) => {
				const passwordRegex =
					/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,50}$/;
				password = password.trim();
				return passwordRegex.test(password);
			}, 'Password must contain at least 1 uppercase letter, 1 lowercase letter, 1 number, and 1 special character.'),
		confirm_password: z.string().min(8).max(50),
		first_name: z.string().max(30),
		last_name: z.string().max(150),
		profile_picture: z
			.any()
			.refine((file) => file?.size <= MAX_FILE_SIZE, 'File is too large')
			.refine((file) => ALLOWED_MIME_TYPES.includes(file?.type), 'File type not allowed')
			.optional()
			.nullable()
			.default(null)
	})
	.refine((data) => data.password === data.confirm_password, {
		message: 'Passwords do not match',
		path: ['confirm_password']
	});

export const load: PageServerLoad = async () => {
	const form = await superValidate(registerSchema);

	return { form };
};

export const actions: Actions = {
	default: async ({ fetch, request }) => {
		const form = await superValidate(request, registerSchema);
		console.log('POST', form);

		if (!form.valid) {
			return fail(400, { form });
		}

		return { form };
	}
};
