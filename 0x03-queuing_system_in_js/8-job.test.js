#!/usr/bin/node
import kue from 'kue';
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

const queue = kue.createQueue();

/* eslint-disable */
describe('createPushNotificationsJobs', () => {
  it('Testing a non array...', () => {
    const job = {
      phoneNumber: '569877867',
      message: 'The verification code is 9667',
    };
    expect(() => createPushNotificationsJobs(job, queue)).to.throw(Error, 'Jobs is not an array');
  });
});
