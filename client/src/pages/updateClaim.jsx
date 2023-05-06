import { useForm } from 'react-hook-form';
import axios from 'axios';
import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import classes from './UpdateClaim.module.css';
import { useNavigate } from 'react-router-dom';

const MOCK_DATA = {
	projectId: '12345',
	firstName: 'Bryan',
	lastName: 'Loh',
	amount: 123,
	currency: 'SGD',
	date: 0,
	purpose: 'For Hackathon',
	claimsId: '123123',
};

const UpdateClaim = () => {
	const { register, handleSubmit, setValue } = useForm();
	const { claimId } = useParams();
	const navigate = useNavigate()

	useEffect(() => {
		console.log(claimId)
		const getClaim = async () => {
			const response = await axios.get(
				`http://localhost:5000/claim/${claimId}`
			);
			console.log(response)
			setValue('projectId', response.data['project_id']);
		setValue('amount', response.data.amount);
		setValue('currency', response.data['currency_id']);
		setValue('date', response.data.date);
		setValue('purpose', response.data.purpose);
		setValue('altDepCode', response.data['alternative_dept_code']);
		};

		getClaim();
		
	}, []);

	const onSubmit = async (data) => {
		const newData = {
			projectId: data.projectId,
			amount: data.amount,
			currency: data.currency,
			date: data.date,
			purpose: data.purpose,
			updateDate: new Date().toISOString(),
			chargeDefault: data.chargetToDept ? data.chargetToDept : false,
			altDepCode: data.altDepCode
		};
		const response = await axios.put(`http://localhost:5000/claims/${claimId}`, {
			data: newData,
		});
		if(response.status === 200) {
			navigate('/dashboard');
		}
	};
	return (
		<div className={classes.body}>
			<form onSubmit={handleSubmit(onSubmit)}>
				<div>
					<label>Project Id</label>
					<input type="text" {...register('projectId')} />
				</div>
				<div>
					<label>Amount</label>
					<input type="text" {...register('amount')} />
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
	);
};

export default UpdateClaim;
