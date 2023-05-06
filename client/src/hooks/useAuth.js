const useAuth = () => {
	const setToken = (token) => {
		document.cookie = `token=${token} ;max-age=${
			60 * 15
		} ;SameSite=Strict `;
	};

	const readToken = () => {
		const token = document.cookie.split('=')[1];
		return token;
	};

	const readTokenHeader = () => {
		return `Bearer ${readToken()}`;
	};

	return { readToken, setToken, readTokenHeader };
};

export default useAuth;
