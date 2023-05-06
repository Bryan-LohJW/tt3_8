import { useForm } from 'react-hook-form';
import useAuth from './../hooks/useAuth';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';
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
	const [error, setError] = useState('');
	const navigate = useNavigate();

	const onSubmit = async (data) => {
		console.log(data.id, data.password);
		const response = await axios.post('http://localhost:5000/login', {
			data: {
				id: data.id,
				password: data.password
			}
		});
		console.log(response)
		if (response.status === 200) {
			const token = response.data.accessToken;
			setToken(token);
			navigate('/dashboard');
		}
		setError('Unauthorized');
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
				<form
					className={classes.form}
					onSubmit={handleSubmit(onSubmit)}
				>
					<div className={classes['input-wrapper']}>
						<label
							className={`${classes['input-label']} ${
								true && classes['input-label-focused']
							}`}
						>
							EmployeeId
						</label>
						<input
							type="text"
							{...register('id')}
							className={classes.input}
						/>
					</div>
					<div className={classes['input-wrapper']}>
						<label
							className={`${classes['input-label']} ${
								true && classes['input-label-focused']
							}`}
						>
							{' '}
							Password
						</label>
						<input
							type="password"
							{...register('password')}
							className={classes.input}
						/>
					</div>
					<input
						type="submit"
						className={`${classes.submit} ${classes.action}`}
						value={'Login'}
					/>
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
