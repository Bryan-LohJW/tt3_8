import { useForm } from 'react-hook-form';
import axios from 'axios';
import classes from './CreateClaim.module.css';
import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

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
	const { claimsId } = useParams();

	useEffect(() => {
		const getClaim = async () => {
			const response = await axios.get(
				`http://localhost:5000/claim/${claimsId}`
			);
			return response.data;
		};

		const data = getClaim();
		setValue('projectId', MOCK_DATA.projectId);
		setValue('amount', MOCK_DATA.amount);
		setValue('currency', MOCK_DATA.currency);
		setValue('date', MOCK_DATA.date);
		setValue('purpose', MOCK_DATA.purpose);
	});

	const onSubmit = async (data) => {
		const newData = {
			projectId: data.projectId,
			amount: data.amount,
			currency: data.currency,
			date: data.date,
			purpose: data.purpose,
			updateDate: new Date(),
		};
		console.log(newData);
		const response = await axios.put('http://localhost:5000/claims', {
			data: newData,
		});
		console.log(response);
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

				<input type="submit" />
			</form>
		</div>
	);
};

export default UpdateClaim;
