import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import Login from './pages/login';
import CreateClaim from './pages/createClaim';
import UpdateClaim from './pages/updateClaim';
import Dashboard from './pages/Dashboard';
import Header from './components/Header';

const router = createBrowserRouter([
	{ path: '/', element: <Login /> },
	{
		element: <Header />,
		children: [
			{ path: '/createClaim', element: <CreateClaim /> },
			{ path: '/updateClaim/:claimId', element: <UpdateClaim /> },
			{ path: '/dashboard', element: <Dashboard /> },
		],
	},
]);

ReactDOM.createRoot(document.getElementById('root')).render(
	<React.StrictMode>
		<RouterProvider router={router} />
	</React.StrictMode>
);
