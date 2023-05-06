import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import Login from './pages/login';
import CreateClaim from './pages/createClaim';
import UpdateClaim from './pages/updateClaim';

const router = createBrowserRouter([
	{ path: '/', element: <Login /> },
	{ path: '/createClaim', element: <CreateClaim /> },
	{ path: '/updateClaim', element: <UpdateClaim /> },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
	<React.StrictMode>
		<RouterProvider router={router} />
	</React.StrictMode>
);
