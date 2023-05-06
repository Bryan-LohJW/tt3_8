import { useForm } from 'react-hook-form';
import axios from 'axios';
import classes from './CreateClaim.module.css';
import { useNavigate } from 'react-router';

const CreateClaim = () => {
	const { register, handleSubmit } = useForm();
	const navigate = useNavigate()

	const onSubmit = async (data) => {
		//console.log(data);
		const response = await axios.post(`http://127.0.0.1:5000/claims`, {
			data: { employeeId: '10010',projectId: data.projectId, amount: data.amount.toFixed(2), currency: data.currency, date: new Date().toISOString(), purpose: data.purpose, chargeDefault: data.chargeDefault, altDepCode: data.altDepCode, last_edit_claim_date: new Date().toISOString(),},
		});
		if(response.status === 200) {
			navigate('')
		}
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
					<label>Amount</label>
					<input type="number" {...register('amount')} />
				</div>
				<div>
					<label>Currency</label>
					<input type="text" {...register('currency')} />
				</div>
				<div>
					<label>Date</label>
					<input type="date" {...register('date')} />
				</div>
				<div>
					<label>Purpose</label>
					<input type="text" {...register('purpose')} />
				</div>
				<div>
					<label>Charge to department</label>
					<input type="checkbox" {...register('chargetToDept')} />
				</div>
				<div>
					<label>Alternate Deparement</label>
					<input type="text" {...register('altDepCode')} />
				</div>
				<input type="submit" />
			</form>
			</div>
		</body>
	);
};

export default CreateClaim;
