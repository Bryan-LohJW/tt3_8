import { useForm } from 'react-hook-form';
import useAuth from './../hooks/useAuth';
import axios from 'axios';
import { Navigate, Link } from 'react-router-dom';
import { useState } from 'react';
import classes from './login.module.css';
import { GoLocation, GoInfo } from 'react-icons/go';
import {
	RiTwitterFill,
	RiFacebookBoxFill,
	RiLinkedinBoxFill,
	RiYoutubeFill,
} from 'react-icons/ri';

const Login = () => {
	const { register, handleSubmit, formState } = useForm();
	const { setToken } = useAuth();
	const [error, setError] = useState();

	const onSubmit = async (data) => {
		console.log(data.email, data.password);
		const response = await axios.post('http://localhost:5000/auth/login', {
			email: data.email,
			password: data.password,
		});
		if (response.status === 200) {
			const token = response.data.accessToken;
			setToken(token);
			Navigate('/dashboard');
		}
		setError(response.data.message);
	};
	return (
		<div className={classes.body}>
			<div className={classes.header}>
				<div></div>
				<div className={classes.links}>
					<Link className={classes.link} to={''}>
						<GoLocation className={classes.icon} />
						Find Us
					</Link>
					<Link className={classes.link} to={''}>
						<GoInfo className={classes.icon} />
						Help & Support
					</Link>
				</div>
			</div>
			<div className={classes.login}>
				<div className={classes.logo}></div>
				<form onSubmit={handleSubmit(onSubmit)}>
					<div className={classes['input-wrapper']}>
						<label
							className={`${classes['input-label']} ${
								false && classes['input-label-focused']
							}`}
						>
							Email
						</label>
						<input type="text" {...register('email')} />
					</div>
					<div className={classes['input-wrapper']}>
						<label
							className={`${classes['input-label']} ${
								false && classes['input-label-focused']
							}`}
						>
							{' '}
							Password
						</label>
						<input type="password" {...register('password')} />
					</div>
					<input type="submit" />
					<span>{error}</span>
				</form>
				<button className={`${classes.help} ${classes.action}`}>
					Get Started
				</button>
				<div className={classes.helpLinks}>
					<p className={classes.helpLink}>
						Forgot <Link to={''}>User ID</Link> or{' '}
						<Link to={''}>PIN</Link>?
					</p>
					<p className={classes.helpLink}>
						<Link to={''}>Frequently Asked Questions</Link>
					</p>
					<p className={classes.helpLink}>
						<Link to={''}>Maintenance Schedule</Link>
					</p>
					<p className={classes.helpLink}>
						<Link to={''}>Security & You</Link>
					</p>
				</div>
			</div>
			<div className={classes.footer}>
				<div className={classes.footerLinks}>
					<Link className={classes.footerLink} to={''}>
						Terms & Conditions
					</Link>
					<Link className={classes.footerLink} to={''}>
						Privacy Policy
					</Link>
					<Link className={classes.footerLink} to={''}>
						Fair Dealing Commitment
					</Link>
					<Link className={classes.footerLink} to={''}>
						Compliance with Tax Requirements
					</Link>
					<Link className={classes.footerLink} to={''}>
						Vulnerable Disclosure Policy
					</Link>
				</div>
				<div className={classes.socials}>
					<RiFacebookBoxFill className={classes.social} />

					<RiTwitterFill className={classes.social} />

					<RiLinkedinBoxFill className={classes.social} />

					<RiYoutubeFill className={classes.social} />
				</div>
			</div>
		</div>
	);
};

export default Login;
