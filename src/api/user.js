import axios from 'axios'

export default {
	async getUsers(path) {
		const endpoint = process.env.API_URL + path
		const response = await axios.get(endpoint)
		.catch(err => {
			return Promise.reject(err.response)
		})
		if (response.status !== 200) {
			let error = error({
				statusCode: response.status,
				message: response.data.message,
			})
			return Promise.reject(error)
		}
		return Promise.resolve(response)
	}
}