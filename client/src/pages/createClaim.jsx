import { useForm } from 'react-hook-form';
import axios from 'axios';
import classes from './CreateClaim.module.css';

const CreateClaim = () => {
	const { register, handleSubmit } = useForm();

	const onSubmit = (data) => {
		console.log(data);
		// axios.post('http://localhost:5000/claims', {
		// 	data: { data },
		// });
	};
	return (
		<body>
		<div className={classes.body}>
			<form onSubmit={handleSubmit(onSubmit)}>
				<div>
					<label>Project Id</label>
					<input type="text" {...register('projectId')} />
				</div>
				<div>
					<label>First Name</label>
					<input type="text" {...register('firstName')} />
				</div>
				<div>
					<label>Last Name</label>
					<input type="text" {...register('lastName')} />
				</div>
				<div>
					<label>Amount</label>
					<input type="number" {...register('amount')} />
				</div>
				<div>
					<label>Currency</label>
					<input type="text" {...register('currency')} />
				</div>
				<div>
					<label>Date</label><br></br>
					<input type="date" {...register('date')} />
				</div>
				<div>
					<label>Purpose</label>
					<input type="text" {...register('purpose')} />
				</div>
				<div>
					<label>Previous Claim Id (if any)</label>
					<input type="text" {...register('claimsId')} />
				</div>
				<input type="submit" />
			</form>
			</div>
		</body>
	);
};

export default CreateClaim;
